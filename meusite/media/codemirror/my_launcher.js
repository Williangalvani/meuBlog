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
//		var pres=previewDiv.find('pre')//addClass("prettyprint");
//		pres.each(
//            function(index, obj) {
//                var prevSibling = this.previousSibling;
//                var nodeValue = null;
//                while (prevSibling && prevSibling.nodeType!==1) {
//                    if (prevSibling.nodeType !== 8) {
////                        alert(obj);
//                        obj.className = "prettyprint";
//                    }
//                    prevSibling = prevSibling.previousSibling;
//                }
//                //console.log(this.innerHTML, nodeValue);
//            }
//        );
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