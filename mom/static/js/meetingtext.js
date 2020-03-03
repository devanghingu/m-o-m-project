function getSelectedText(e)
{
   selectedtext="";
   
   if(window.getSelection().toString().length>7)
   {
      selectedtext = window.getSelection().toString();
      
      newli=$(document.createElement('li'));
      newli.addClass('list-group-item');
      newli.attr('draggable','true');
      newli.attr('role','option');
      newli.attr('aria-grabbed','false');

      newli.html(selectedtext);
      
      $('.sortable').append(newli);
   }
}
total_node=[]
function get_total_node(list=[])
{
}
function showButton(e){
   e.stopPropagation();
   var meetingtext=document.getElementById("meetingtext");
   var tar = e.target.getBoundingClientRect();
   if(window.getSelection().toString().length >=8 )
   {
      $('.showbtn').css({
         top : 8+ e.clientY,
         left : 12+e.clientX
      }).show();
   }
   else{
      $('.showbtn').hide();
   }
}
$(document).on("click", function(e) {
   e.stopPropagation();
   $('.showbtn').hide();
});

let item=[];
$('#done').click(function(){
   $('.sortable').each(function(){
      $(this).find('li').each(function(){
         item.push($(this).text());
      });
   });
});


$(document).ready(function(){
   var meeting_text = $('#meetingtext').text();
   obj = JSON.parse(localStorage.getItem('response_text'));
   for(txt of obj.response_text){
      meeting_text += txt;   
   }
   $('#meetingtext').text(meeting_text);
});