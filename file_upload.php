<?php
	$check = getimagesize($_FILES["file_tobe"]["tmp_name"]);
    if($check !== false){
        $image = $_FILES['file_tobe']['tmp_name'];
        $imgContent = addslashes(file_get_contents($image));
		
		$s="";
        $id=$_SESSION['Userid'];
		date_default_timezone_get("Asia/Kolkata");
        $dataTime = date("Y-m-d H:i:s");
		$q1=set_progress('img');
		$q2=set_bits('img');
        $insert = mysqli_query($con,"Update Candidates SET Progress='$q1',Status_bits='$q2',Image='$imgContent',Created='$dataTime' where Email='$id'");
		$sql="Select * from Candidates Where Email='$id'";
        if($insert)
		{
			$result=mysqli_query($con,$sql);
			if($result)
			{
				$row=mysqli_fetch_array($result);
				$im='<img class="img-responsive img-circle" style="height:150px;" src="data:image/jpeg;base64,'.base64_encode($row['Image']).'"/>'; 
				$s="<span style='color:green;'>Profile Picture Set.</span><br/><br/>
				<a class='btn btn-primary' href='candidate_profile.php'>Next</a>";
			}
			else
			{
				$s= "<span style='color:red;'>Profile Picture upload failed.</span>
				 please <a class='btn btn-primary' href='candidate_upload_img.php'>try again</a>";
			}
        }else{
			
           	$s= "<span style='color:red;'>Profile Picture upload failed.</span>
			 please <a class='btn btn-primary' href='candidate_upload_img.php'>try again</a>";
        }
    }else{
        $s= "<span style='color:red;'>Profile Picture upload failed.</span>
			 please <a class='btn btn-primary' href='candidate_upload_img.php'>try again</a>";
    }
?>