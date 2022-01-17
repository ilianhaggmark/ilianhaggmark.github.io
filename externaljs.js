
//CODE TO SHOW/HIDE CONTENT EPAPERS/PRESENTATIONS 
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
  
// CODE TO CHANGE CONTRAST MODE
function changeContrastMode() {
   var element = document.body;
   element.classList.toggle("contrast-mode");
}
