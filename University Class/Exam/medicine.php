<?php

	mysql_connect('localhost', 'root', 'root');
	
	mysql_select_db('tuhin');
	
	$name = $_POST['medi_name'];
	
	$manufacture = $_POST['manu'];
	
	$batch_no = $_POST['batch'];
	
	$manufacture_date = $_POST['manu_date'];
	
	$expiry_date = $_POST['expiry_date'];
	
	$add = "insert into users (medi_name, manu, batch, manu_date,
	expiry_date) value ('$name', '$manufacture', '$batch_no', 
	'$manufacture_date', '$expiry_date')";
	
	$update = "update users SET medi_name =[$name], manu
	=[$manufacture], batch=[$batch_no], manu_date = [$manufacture_date],
	expiry_date =[$expiry_date] WHERE 1";
	
	$delete = "DELETE FROM users WHERE 0";
	
	$search = "SELECT * FROM users WHERE medi_name LIKE 'Napa'";
	
	
	if(mysql_query($add))
		{
			
			echo "Add Success Fully Done";
		}
	
	else if(mysql_query($update))
		
		{
			echo "Update Success Fully Done";
			
		}
		
	else if(mysql_query($delete))
		
		{
			echo "Delete Success Fully Done";
			
		}
		
	else if(mysql_query($search))
		
		{
			echo "Search Success Fully Done";
			
		}



?>