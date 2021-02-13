<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title> Günün Bölümleri </title>
</head>
<body>

	<?php

	$saat=date("H:i");

	if($saat>="06:00" and $saat<"10:00") {
		echo "Günaydın...";
	} 
	elseif($saat>="10:00" and $saat<"17:00") {
		echo "İyi günler...";
	}  
	elseif($saat>="17:00" and $saat<"20:00") {
		echo "İyi akşamlar...";
	}  
	elseif($saat>="20:00" and $saat<"00:00") {
		echo "İyi geceler..";
	}  
	elseif($saat>="00:00" and $saat<"06:00") {
		echo "Eshenlikler dilerim...";
	}

	?>

</body>
</html>