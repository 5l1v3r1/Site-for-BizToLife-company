tinyMCE.init({
    mode:"textareas",
    language : "ru",
    toolbar : 'undo redo | styleselect | fontselect fontsizeselect | fullpage image media emoticons link unlink paste bold forecolor backcolor alignleft italic aligncenter alignright alignjustify outdent indent bullist numlist visualchars visualblocks ltr rtl code fullscreen | template hr anchor help',
    plugins : 'image link media autolink emoticons hr anchor textcolor paste importcss imagetools fullpage contextmenu help visualchars visualblocks directionality table autosave save code fullscreen lists template',

    // Theme options
    theme_advanced_buttons1 : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,bullist,numlist,sub,sup,|,forecolor,backcolor,formatselect,fontsizeselect",
    theme_advanced_buttons2 : "outdent,indent,|,undo,redo,|,link,unlink,anchor,image,tablecontrols,removeformat,code",
    theme_advanced_toolbar_location : "top",
    theme_advanced_toolbar_align : "left",
    theme_advanced_statusbar_location : "bottom",
    theme_advanced_resizing : true
});
