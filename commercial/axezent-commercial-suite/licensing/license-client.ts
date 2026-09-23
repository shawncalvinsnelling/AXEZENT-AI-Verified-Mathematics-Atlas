export type EntitlementResult = {
  allowed: boolean;
  productId: string;
  expiresAt?: string;
  features?: string[];
  reason?: string;
};

export type EntitlementConfig = {
  serverUrl: string;
  productId: string;
  licenseKey: string;
  installationId: string;
  version: string;
  timeoutMs?: number;
};

export class EntitlementError extends Error {
  constructor(message: string, public result?: EntitlementResult) {
    super(message);
    this.name = "EntitlementError";
  }
}

const cache = new Map<string, { at: number; value: EntitlementResult }>();
const CACHE_MS = 5 * 60 * 1000;

export async function checkEntitlement(cfg: EntitlementConfig): Promise<EntitlementResult> {
  const key = [cfg.serverUrl, cfg.productId, cfg.licenseKey, cfg.installationId].join("|");
  const hit = cache.get(key);
  if (hit && Date.now() - hit.at < CACHE_MS) return hit.value;

  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), cfg.timeoutMs ?? 8000);

  try {
    const res = await fetch(new URL("/v1/entitlements/check", cfg.serverUrl), {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "authorization": `Bearer ${cfg.licenseKey}`
      },
      body: JSON.stringify({
        productId: cfg.productId,
        installationId: cfg.installationId,
        version: cfg.version
      }),
      signal: controller.signal
    });

    if (!res.ok) {
      return { allowed: false, productId: cfg.productId, reason: `entitlement_http_${res.status}` };
    }

    const value = await res.json() as EntitlementResult;
    cache.set(key, { at: Date.now(), value });
    return value;
  } catch {
    return { allowed: false, productId: cfg.productId, reason: "entitlement_unavailable" };
  } finally {
    clearTimeout(timer);
  }
}

export async function assertEntitled(cfg: EntitlementConfig, feature?: string) {
  const result = await checkEntitlement(cfg);
  const featureAllowed = !feature || (result.features ?? []).includes(feature);

  if (!result.allowed || !featureAllowed) {
    throw new EntitlementError(
      result.reason ?? (feature ? `feature_not_entitled:${feature}` : "subscription_inactive"),
      result
    );
  }

  return result;
}
