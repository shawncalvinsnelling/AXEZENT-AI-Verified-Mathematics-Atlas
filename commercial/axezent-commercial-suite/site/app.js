const input = document.getElementById("sInput");
const button = document.getElementById("runButton");
const result = document.getElementById("result");

function interior(s,k){
  const two=2n;
  const num=k**3n-4n*k**2n*s-3n*k**2n+4n*k*s**2n+8n*k*s+6n*k-4n*s**2n-6n*s-4n;
  if(num%two!==0n) throw new Error("Non-integral coefficient");
  return num/two;
}
function pCoeffs(s){
  const out=[s*(s+1n)/2n,(3n*s*s-s+2n)/2n,(5n*s*s-7n*s+4n)/2n];
  for(let k=3n;k<=2n*s;k++) out.push(interior(s,k));
  out.push(s);
  return out;
}
function timesOnePlusX(a){
  const out=Array(a.length+1).fill(0n);
  a.forEach((v,i)=>{out[i]+=v;out[i+1]+=v;});
  return out;
}
function unimodal(a){
  let max=a[0]; for(const x of a) if(x>max) max=x;
  const first=a.findIndex(x=>x===max);
  let last=first; for(let i=first;i<a.length;i++) if(a[i]===max) last=i;
  for(let i=0;i<first;i++) if(a[i]>a[i+1]) return false;
  for(let i=first;i<=last;i++) if(a[i]!==max) return false;
  for(let i=last;i<a.length-1;i++) if(a[i]<a[i+1]) return false;
  return true;
}
function strictLC(a){
  for(const x of a) if(x<=0n) return false;
  for(let i=1;i<a.length-1;i++) if(a[i]*a[i] <= a[i-1]*a[i+1]) return false;
  return true;
}
async function sha256(text){
  if(!crypto?.subtle) return "unavailable in this browser context";
  const bytes=new TextEncoder().encode(text);
  const hash=await crypto.subtle.digest("SHA-256",bytes);
  return [...new Uint8Array(hash)].map(x=>x.toString(16).padStart(2,"0")).join("");
}
button.addEventListener("click",async()=>{
  try{
    if(!/^\d+$/.test(input.value.trim())) throw new Error("Enter an integer s ≥ 1.");
    const s=BigInt(input.value.trim());
    if(s<1n) throw new Error("Enter an integer s ≥ 1.");
    if(s>10000n) throw new Error("Browser demo limit is s ≤ 10,000.");
    const p=pCoeffs(s), b=timesOnePlusX(p);
    const payload={
      schema:"axezent.six_cycle.browser.v1",
      source:"Snelling_Six_Cycle_Hook_Unimodality_2026-09-22",
      family:"(6^s)",
      s:s.toString(),
      m_shift:(2n*s-1n).toString(),
      p_coefficients:p.map(String),
      checks:{
        positive_support:p.every(x=>x>0n),
        unimodal:unimodal(p),
        strict_log_concavity_after_one_plus_x:strictLC(b)
      },
      scope:"Published all-s six-cycle family only; not the full arbitrary-partition conjecture."
    };
    payload.sha256=await sha256(JSON.stringify(payload));
    result.textContent=JSON.stringify(payload,null,2);
  }catch(err){result.textContent="Error: "+err.message;}
});
