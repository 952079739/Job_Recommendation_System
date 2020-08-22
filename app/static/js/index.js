//点击城市添加active
$("#city_id dd").click(function(){
	$("#city_id dd").removeClass("active");
	$(this).addClass("active");
})

//点击工作性质添加active
$("#work_id dd").click(function(){
	$("#work_id dd").removeClass("active");
	$(this).addClass("active");
})

//点击投递属性添加active
$("#property_id dd").click(function(){
	$("#property_id dd").removeClass("active");
	$(this).addClass("active");
})

//点击职能类型添加active
$("#function_id dd").click(function(){
	$("#function_id dd").removeClass("active");
	$(this).addClass("active");
})

//点击企业性质添加active
$("#enterprise_id dd").click(function(){
	$("#enterprise_id dd").removeClass("active");
	$(this).addClass("active");
})

//点击行业性质添加active
$("#industry_id dd").click(function(){
	$("#industry_id dd").removeClass("active");
	$(this).addClass("active");
})

//点击行业性质添加active
$("#sort_id span").click(function(){
	$("#sort_id span").removeClass("active");
	$(this).addClass("active");
})