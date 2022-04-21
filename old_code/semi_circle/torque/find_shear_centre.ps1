#initial
$ScriptOutput = 0.1
$loading_z = 0
$sim_number = 0

while($loading_z -lt 60)
    {
        python intermediate.py 1.0 $loading_z

        $sim_number =  $sim_number + 1
        Write-Output ("Simulation Number : {0}" -f ($sim_number))
        Write-Output ("Loading Position: {0}/59" -f ($loading_z) )

        abaqus cae script=semi-circle_script.py

        $find_shear_center= "C:\Users\touze\project\Shear_centre\semi_circle\torque\find_shear_centre_rotation.py"
        $ScriptOutput=[double]$( python $find_shear_center)
        Write-Output ("shear centre" -f ($ScriptOutput) )

        $entry  = [pscustomobject]@{
                "loading_z" = $loading_z
                "shear centre" = $ScriptOutput
            }

        $entry | Export-CSV  "E:\temp\SC\outfile.csv" -Append

        $loading_z = $loading_z + 1
    }
