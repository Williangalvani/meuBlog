$(function(){
			setTimeout(function(){
					$(window).scrollTop($.cookie('django_admin_scroll'));
					$.cookie('django_admin_scroll', 0);
				}, 100);
		});
		function save_and_continue(){
			$.cookie('django_admin_scroll',$(window).scrollTop());
			$('input[name="_continue"]').click()
			console.log("worked");
		}
		$(document).bind('keydown', "Ctrl+S", save_and_continue)


