!function(e){function t(e,t){var n=new Image,r=e.getAttribute("data-src");n.onload=function(){e.parent?e.parent.replaceChild(n,e):e.src=r,t&&t()},n.src=r}for(var n=new Array,r=function(e,t){if(document.querySelectorAll)t=document.querySelectorAll(e);else{var n=document,r=n.styleSheets[0]||n.createStyleSheet();r.addRule(e,"f:b");for(var l=n.all,c=0,o=[],a=l.length;c<a;c++)l[c].currentStyle.f&&o.push(l[c]);r.removeRule(0),t=o}return t}("img.lazy"),l=function(){for(var r=0;r<n.length;r++)(l=n[r].getBoundingClientRect()).top>=0&&l.left>=0&&l.top<=(e.innerHeight||document.documentElement.clientHeight)&&t(n[r],function(){n.splice(r,r)});var l;},c=0;c<r.length;c++)n.push(r[c]);l(),function(t,n){e.addEventListener?this.addEventListener(t,n,!1):e.attachEvent?this.attachEvent("on"+t,n):this["on"+t]=n}("scroll",l)}(this);