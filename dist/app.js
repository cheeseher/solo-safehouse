'use strict';
// Native links/details remain usable without JavaScript.
const dialog = document.querySelector('#lightbox');
const lightImage = document.querySelector('#lightbox-image');
const stage = document.querySelector('.lightbox-stage');
const zoom = document.querySelector('#zoom-toggle');
let lastTrigger = null;
function resetZoom(){stage.classList.remove('zoomed');zoom.textContent='放大细节';zoom.setAttribute('aria-pressed','false');stage.scrollTop=0;stage.scrollLeft=0;}
if(dialog && typeof dialog.showModal === 'function'){
 document.addEventListener('click',event=>{
  const link=event.target.closest('[data-lightbox]');
  if(!link||event.ctrlKey||event.metaKey||event.shiftKey||event.altKey)return;
  event.preventDefault();lastTrigger=link;
  const caption=link.dataset.caption||link.querySelector('img')?.alt||'设计大图';
  lightImage.src=link.href;lightImage.alt=caption;
  document.querySelector('#lightbox-caption').textContent=caption;
  document.querySelector('#lightbox-original').href=link.href;
  resetZoom();dialog.showModal();document.documentElement.classList.add('no-scroll');
 });
 document.querySelector('#lightbox-close').addEventListener('click',()=>dialog.close());
 dialog.addEventListener('click',e=>{if(e.target===dialog)dialog.close();});
 dialog.addEventListener('close',()=>{document.documentElement.classList.remove('no-scroll');resetZoom();lastTrigger?.focus({preventScroll:true});});
 zoom.addEventListener('click',()=>{const active=stage.classList.toggle('zoomed');zoom.textContent=active?'适合屏幕':'放大细节';zoom.setAttribute('aria-pressed',String(active));});
}
const plans={layout:['全屋布局','布局图 / 柜号与下方收纳图一一对应，点图可放大。'],life:['生活动线','绿色线表示典型生活路径：回家、用餐、洗浴与休息。为示意连接，非所有人的唯一走法。'],robot:['机器人清扫','绿色为主要连接；棕色虚线为有条件开放的卫浴干区。淋浴、设备间和室外不纳入清扫；路线不等于实际算法轨迹。']};
const tabs=[...document.querySelectorAll('[data-plan]')];
function selectPlan(tab){
 const key=tab.dataset.plan, panel=document.querySelector('#plan-panel'),link=panel.querySelector('a'),img=panel.querySelector('img');
 tabs.forEach(t=>{t.setAttribute('aria-selected',String(t===tab));t.tabIndex=t===tab?0:-1;});
 panel.setAttribute('aria-labelledby',tab.id);link.href=`assets/plan-${key}.svg`;link.dataset.caption=`安全屋概念平面 / ${plans[key][0]}`;img.src=link.getAttribute('href');img.alt=link.dataset.caption;document.querySelector('#plan-caption').textContent=plans[key][1];
}
tabs.forEach((tab,index)=>{tab.addEventListener('click',()=>selectPlan(tab));tab.addEventListener('keydown',event=>{let next;if(event.key==='ArrowRight')next=(index+1)%tabs.length;else if(event.key==='ArrowLeft')next=(index+tabs.length-1)%tabs.length;else if(event.key==='Home')next=0;else if(event.key==='End')next=tabs.length-1;else return;event.preventDefault();tabs[next].focus();selectPlan(tabs[next]);});});
function openHash(){let id;try{id=decodeURIComponent(location.hash.slice(1));}catch{return;}const target=document.getElementById(id);if(target instanceof HTMLDetailsElement){target.open=true;requestAnimationFrame(()=>target.scrollIntoView({block:'start'}));}}
window.addEventListener('hashchange',openHash);openHash();
document.querySelectorAll('a[href^="#cab-"]').forEach(link=>link.addEventListener('click',()=>{const el=document.getElementById(link.hash.slice(1));if(el)el.open=true;}));
if('IntersectionObserver' in window){const navLinks=[...document.querySelectorAll('.site-header nav a')];const observer=new IntersectionObserver(entries=>{entries.forEach(e=>{if(!e.isIntersecting)return;navLinks.forEach(a=>{if(a.hash==='#'+e.target.id)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});});},{rootMargin:'-15% 0px -65% 0px'});navLinks.forEach(a=>{const el=document.querySelector(a.hash);if(el)observer.observe(el);});}
