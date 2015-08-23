$("#btn_submit").click(function(){
	$("#target").submit();
})

function LogUserFeedback(value){
	
	if (value == "success")
	{
		console.log("suuuucesso!");
	}
	else if(value == "error")
	{
		console.log("cagou");
	}
	else
	{
		console.log("fail");
	}
}
