<?php

$fname = $_POST["fname"];
$lname = $_POST["lname"];
$email = $_POST["email"];

$errors = [];

if(! $fname){
	$errors[] = "First name must be submitted";
}
if(! $lname){
	$errors[] = "Last name must be sumbitted";
}
if(! $email){
	$errors[] = "Email must be submitted";
}

if(!empty($errors)){
	die(implode("<br>", $errors));
}

else
{
	$host = "wikix-db.cjgssw28mq1e.us-west-1.rds.amazonaws.com";
	$dbname = "WikiX_Users";
	$username = "masterWiki";
	$password = "masterWiki29!";

	$conn = mysqli_connect(hostname : $host, 
		username : $username, 
		password : $password, 
		database : $dbname);


	if(mysqli_connect_errno()) {
		die("Connection error: " . mysqli_connect_error());
	}

	$sql = "INSERT INTO userProfile (fName, lName, email)
			VALUES(?, ?, ?)";
	$stmt = mysqli_stmt_init($conn);

	if(! mysqli_stmt_prepare($stmt, $sql)) {
		die(mysqli_error($conn));
	}
	
	mysqli_stmt_bind_param($stmt, "sss",
						   $fname,
						   $lname,
						   $email);
	mysqli_stmt_execute($stmt);

	echo "Record saved.";
	header("Location: subscribed.htm");
}

?>