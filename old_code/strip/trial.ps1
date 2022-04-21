$outfile = "E:\temp\Outfile.csv"
$newcsv = {} | Select "EMP_Name","EMP_ID","CITY" | Export-Csv $outfile
$csvfile = Import-Csv -Path $outfile
$csvfile.Emp_Name = "Charles"
$csvfile.EMP_ID = "2000"
$csvfile.CITY = "New York"
$csvfile | Export-CSV $outfile

$csvfile = Import-Csv -Path $outfile
$csvfile.Emp_Name = "Charley"
$csvfile.EMP_ID = "2002"
$csvfile.CITY = "New York"
$csvfile | Export-CSV -append $outfile
# $outfile Import-Csv $outfile


