#initial
$ScriptOutput = 0.1
$d = 0
$sim_number = 0

while($d -lt 8)
    {
        python intermediate.py $d

        $sim_number =  $sim_number + 1
        Write-Output ("Simulation Number : {0}" -f ($sim_number))
        Write-Output ("Loading Position: {0}/59" -f ($d) )

        abaqus cae noGUI=box_script.py

        $find_warping= "C:\Users\touze\project\Shear_centre\box_section\varying_warping\warping_analysis.py"
        $ScriptOutput=[double]$( python $find_warping)
        Write-Output ("warping z" -f ($ScriptOutput) )

        $entry  = [pscustomobject]@{
                "d" = $d
                "warping z" = $ScriptOutput
            }

        $entry | Export-CSV  "E:\temp\box\outfile.csv" -Append

        $d = $d + 1
    }
