django.jQuery(document).ready(function()
{
myTextArea = django.jQuery("textarea.codemirror");
var editor = CodeMirror.fromTextArea(myTextArea.get(0),
      {
          mode: {name: "markdown"},
          lineWrapping: true,
    });


    editor.on("change", updatePreview);
	editor.on("scroll", scrollPreview);
	//convert = new Markdown.Converter().makeHtml;
	converter = new Markdown.Converter();
	var previewDiv = django.jQuery('.wmd-preview');
	function updatePreview() {
		var mhtml=converter.makeHtml(editor.getValue())	;
		previewDiv.html(mhtml);
		console.log(mhtml);
		console.log(previewDiv);

	}
	function scrollPreview(){
		var percent=editor.getScrollerElement().scrollTop/editor.getScrollerElement().scrollHeight;
		console.log(percent);
				previewDiv.scrollTop=percent*previewDiv.scrollHeight;
	}
	updatePreview();
});