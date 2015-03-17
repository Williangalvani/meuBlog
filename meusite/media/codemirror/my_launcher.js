django.jQuery(document).ready(function()
{
myTextArea = django.jQuery("textarea.codemirror");
var editor = CodeMirror.fromTextArea(myTextArea.get(0),
      {
          mode: {name: "markdown"},
          extraKeys: {
          "Ctrl-S" : function(instance){
          $('input[name="_continue"]').click();
          $.cookie('django_admin_scroll',$(window).scrollTop());
          }
          },
          lineWrapping: true,
    });


    editor.on("change", updatePreview);
	editor.on("scroll", scrollPreview);
	converter = new Markdown.Converter();
	var previewDiv = django.jQuery('.wmd-preview');
	function updatePreview() {
		var mhtml=converter.makeHtml(editor.getValue())	;
		previewDiv.html(mhtml)
		PR.prettyPrint();
	}
	function scrollPreview(){
		var percent=editor.getScrollerElement().scrollTop/editor.getScrollerElement().scrollHeight;
		console.log(percent);
				previewDiv.scrollTop=percent*previewDiv.scrollHeight;
	}
	updatePreview();
	PR.prettyPrint();
});


$(function(){
			setTimeout(function(){
					$(window).scrollTop($.cookie('django_admin_scroll'));
					$.cookie('django_admin_scroll', 0);
				}, 100);
		});


//when the document is ma

function doPreLoad(){
            $('input[name="_continue"]').click();
          $.cookie('django_admin_scroll',$(window).scrollTop());
          }

$(function(){

  //create an event handler for the mousemove
  var preLoadTimer;
  $(this).mousemove(function(e){
    //clear prior timeout, if any
    window.clearTimeout(preLoadTimer);

    //create new timeout.
    preLoadTimer = window.setTimeout(doPreLoad, 20000);
  });

});