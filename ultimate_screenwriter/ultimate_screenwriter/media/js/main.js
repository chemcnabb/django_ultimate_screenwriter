var SCRIPT_FORMAT_LIST = ("action", "character", "parentheses", "dialogue", "heading");

var delay = (function(){
   var timer = 0;
   return function(callback, ms){
       clearTimeout (timer);
       timer = setTimeout(callback, ms);
   };
})();


function doScriptResize(vvar){
   var iFrame = $(".jHtmlArea > div > iframe");
   var jHtmlArea = $(".jHtmlArea");
   var screenplay_container = $("#screenplay-container");

   //jHtmlArea.width(vvar-25);
   //iFrame.width(vvar-25);
}


function scriptFormat(edit_mode, executor){
   switch(edit_mode)
   {
       case "heading":
           executor.execCommand("formatBlock", false, "<h1>");
           break;
       case "action":
           executor.execCommand("formatBlock", false, "<div>");
           break;
       case "character":
           executor.execCommand("formatBlock", false, "<h2>");
           break;
       case "parentheses":
           executor.execCommand("formatBlock", false, "<h4>");
           break;
       case "dialogue":
           executor.execCommand("formatBlock", false, "<h3>");
           break;

   }
   return edit_mode;
}

function insertAtCaret(areaId,text) {
   var txtarea = document.getElementById(areaId);
   var scrollPos = txtarea.scrollTop;
   var strPos = 0;
   var br = ((txtarea.selectionStart || txtarea.selectionStart == '0') ?
       "ff" : (document.selection ? "ie" : false ) );
   if (br == "ie") {
       txtarea.focus();
       var range = document.selection.createRange();
       range.moveStart ('character', -txtarea.value.length);
       strPos = range.text.length;
   }
   else if (br == "ff") strPos = txtarea.selectionStart;

   var front = (txtarea.value).substring(0,strPos);
   var back = (txtarea.value).substring(strPos,txtarea.value.length);
   txtarea.value=front+text+back;
   strPos = strPos + text.length;
   if (br == "ie") {
       txtarea.focus();
       var range = document.selection.createRange();
       range.moveStart ('character', -txtarea.value.length);
       range.moveStart ('character', strPos);
       range.moveEnd ('character', 0);
       range.select();
   }
   else if (br == "ff") {
       txtarea.selectionStart = strPos;
       txtarea.selectionEnd = strPos;
       txtarea.focus();
   }
   txtarea.scrollTop = scrollPos;
}
