  
// CODE TO CHANGE CONTRAST MODE
function changeContrastMode() {
   var element = document.body;
   element.classList.toggle("contrast-mode");
   if(document.body.classList.contains('contrast-mode')){
       localStorage.setItem('contrastMode','true');
   } else{
       localStorage.setItem('contrastMode','false');
   }
}

if ( localStorage.getItem('contrastMode') == 'true' ) {  
  document.body.classList.add('contrast-mode');

  // Used for skolmatriklar
  var element = document.getElementById('svg');
  element.classList.add("contrast-mode");
}

// Used for skolmatriklar
function changeContrastModeSvg() {
  console.log('HEJ')
  var element = document.getElementById('svg');
  element.classList.toggle("contrast-mode");
}

//CODE TO SHOW/HIDE (COLLAPSE) CONTENT, E.G. PAPERS/PRESENTATIONS 
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}
