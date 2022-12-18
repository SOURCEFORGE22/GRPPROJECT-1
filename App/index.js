!function()
{"use strict";
    function t(t,e,n=.001)
    {
    return Math.abs(t-e)<n}
    function e(t,e)
    {return window.getComputedStyle(t).getPropertyValue(e)}
    function n(t,e,n)
    {t.style.setProperty(e,n)}
    function o(t,n)
    {const o=document.createElement("div");
    o.style.setProperty(t,n),document.body.append(o);
    const r=e(o,t);
    return o.remove(),r}
    function r()
    {const r=function(){const t=parseFloat(o("font-size","0.1px"));
    return t>1?t:0}(),i=function(t)
    {const e=2*Math.max(t,1);
    return e/parseFloat(o("font-size",`${e}px`))}
    (r);
    if(function(t)
    {if(0===t)return;
    n(document.documentElement,"--minfs",`${t}px`);
    const e=()=>{const e=100*t,{clientWidth:o}=document.documentElement;
    n(document.documentElement,"--rzf",e>o?(o/e).toPrecision(4):null)};
    window.addEventListener("resize",e),e()}
    (r*Math.max(1,i)),t(i,1))return;
    const c=t(parseFloat(e(document.documentElement,"font-size")),parseFloat(o("grid-template-columns","1rem")));
    n(document.documentElement,c?"--rfso":"--bfso",i.toPrecision(4))}
    var i;
    
    const c="undefined"!=typeof window?null===(i=window.navigator)||void 0===i?void 0:i.userAgent:void 0;
    const a=!(!c||(d=c,!d.match(/AppleWebKit\//)||d.match(/Chrome\//)||d.match(/Chromium\//)));
    var d;
    function s(t)
    {var e,n,o,r;
    if(0!==t.getBoundingClientRect().width)return;
    const i=Array.from(t.children).map((t=>t));
    i.forEach(((t,e)=>{if(t.hasAttribute("data-foreign-object-container"))t.style.transformOrigin="",t.style.transform="",t.style.clipPath="";
    else{const n=document.createElement("div");
    n.setAttribute("data-foreign-object-container",""),n.style.willChange="transform",t.insertAdjacentElement("beforebegin",n),t.remove(),n.append(t),i[e]=n}}));
    const c=t.closest("svg"),a=null==c?void 0:c.getBoundingClientRect(),d=t.getScreenCTM();
    if(!d||!a)return;const{a:s,b:u,c:l,d:m,e:f,f:p}=d,v=null!==(n=null===(e=t.x)||void 0===e?void 0:e.baseVal.value)&&void 0!==n?n:0,g=null!==(r=null===(o=t.y)||void 0===o?void 0:o.baseVal.value)&&void 0!==r?r:0;
    i.forEach((t=>{if(!t.hasAttribute("data-foreign-object-container"))return;
    const{style:e}=t;
    e.transformOrigin=`${-v}px ${-g}px`,e.transform=`matrix(${s}, ${u}, ${l}, ${m}, ${f-a.left}, ${p-a.top})`;
    const n=(a.top-p)/s,o=(a.left-f)/s,r=n+a.height/s,i=o+a.width/s;
    e.clipPath=`polygon(${o}px ${n}px, ${i}px ${n}px, ${i}px ${r}px, ${o}px ${r}px)`}))}
    function u()
    {const t=document.querySelectorAll("foreignObject");
    Array.from(t).forEach(s)}[function(){"loading"===document.readyState?window.addEventListener("DOMContentLoaded",r):r()},
                            function(){a&&(window.addEventListener("resize",u),"loading"===document.readyState?window.addEventListener("DOMContentLoaded",u):u())}].forEach((t=>t()))}();

                            window.C_CAPTCHA_IMPLEMENTATION = 'RECAPTCHA';
window.C_CAPTCHA_KEY = '6Ldk59waAAAAAMPqkICbJjfMivZLCGtTpa6Wn6zO';
const lang = navigator.language ? navigator.language : 'en';

fetch('_footer?lang=' + encodeURIComponent(lang)).then(response => {
    response.text().then(footerStr => {
    const div = document.createElement('div');
    div.innerHTML = footerStr;
    for (const child of [...div.children]) {
        if (child.tagName.toLowerCase() !== 'script') {
        document.body.append(child);
        }
    }

    (() => { !function(){"use strict";const e=document.getElementById("modal_backdrop"),t=document.getElementById("report_form"),o=document.getElementById("report_button"),n=document.getElementById("form_report"),c=document.getElementById("form_cancel"),s=document.getElementById("form_submit_reason"),a=document.getElementById("form_go_back"),d=document.getElementById("form_submit_captcha"),l=document.getElementById("form_close"),i=document.getElementById("report_reason_0"),r=document.getElementById("error_message"),m=document.getElementById("error_message_captcha"),u=[document.getElementById("form_step_terms"),document.getElementById("form_step_report_reason"),document.getElementById("form_step_captcha"),document.getElementById("form_step_success")];function p(){e.classList.remove("active"),t.classList.remove("active"),o.classList.remove("active"),o.focus()}function E(e){u.forEach(((t,o)=>{t.style.display=o===e?"block":"none"}))}let _,y=!1;const f="NETEASE"===window.C_CAPTCHA_IMPLEMENTATION?()=>_:()=>{const e=t.elements.namedItem("g-recaptcha-response");return null==e?void 0:e.value};e.onclick=p,c.onclick=p,l.onclick=p,o.onclick=function(){u.forEach(((e,t)=>{e.style.display=0===t?"block":"none"})),e.classList.add("active"),t.classList.add("active"),o.classList.add("active"),i.checked=!0,setTimeout((()=>{i.focus()}),350)},n.onclick=()=>E(1),s.onclick=()=>{E(2),function(){if(y)return;const e=document.createElement("script");console.log("our window captcha: ",window.C_CAPTCHA_IMPLEMENTATION,window.C_CAPTCHA_KEY),e.src="NETEASE"===window.C_CAPTCHA_IMPLEMENTATION?"https://cstaticdun.126.net/load.min.js":"https://www.google.com/recaptcha/api.js",e.async=!0,e.defer=!0,document.head.appendChild(e),y=!0,e.onload="NETEASE"===window.C_CAPTCHA_IMPLEMENTATION?()=>{var e;null===(e=window.initNECaptcha)||void 0===e||e.call(window,{captchaId:window.C_CAPTCHA_KEY,element:"#netease-captcha",protocol:"https",width:"auto",onVerify:(e,t)=>{_=t.validate}})}:()=>{}}()},a.onclick=()=>E(1),t.addEventListener("submit",(function(e){e.preventDefault(),r.style.display="none",m.style.display="none";const t=function(){let e="";const t=document.getElementsByName("report_reason");for(let o=0;o<t.length;o++){const n=t[o];!0===n.checked&&(e=n.value)}return e}(),o=f();if(!o)return void(m.style.display="block");const n={reason:t,challenge:o},c=window.location.origin+window.location.pathname+"/_api/report";d.classList.add("loading"),fetch(c,{method:"POST",body:JSON.stringify(n),headers:{"Content-Type":"application/json; charset=utf-8"}}).then((e=>{d.classList.remove("loading"),e.ok?E(3):r.style.display="block"}))}))}(); })();
    });
});
