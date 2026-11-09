(function(){
  var root=document.documentElement;
  // bille de billard qui roule le long du rail selon la lecture
  function prog(){var h=root.scrollHeight-innerHeight;root.style.setProperty('--p',h>0?Math.min(1,scrollY/h):0)}
  addEventListener('scroll',prog,{passive:true});addEventListener('resize',prog);prog();
  // apparition discrète
  var els=[].slice.call(document.querySelectorAll('.rv'));
  if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in')});return}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px'});
  els.forEach(function(e){io.observe(e)});
})();
