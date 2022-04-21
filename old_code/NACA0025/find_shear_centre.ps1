
#initial
$LB = -0.3
$UB = -0.1
$ScriptOutput = 0.1

$increment =  0.000001

$loading_z = 0
$sim_number = 0
while($loading_z -lt 60)
    {
        while(($UB-$LB -gt $increment) )
        {
            $a = ($UB-$LB)/2
            $trial = $LB+$a

            python intermediate.py $trial $loading_z

            $sim_number =  $sim_number + 1
            Write-Output ("Simulation Number : {0}" -f ($sim_number))
            Write-Output ("Loading Position: {0}/59" -f ($loading_z) )

            abaqus cae noGUI=NACA0025_script.py

            $find_shear_center="C:\Users\touze\project\Shear_centre\NACA0025\find_shear_centre.py"
            $ScriptOutput=[double]$( python $find_shear_center)

            $range = $UB-$LB
            Write-Output ("Range : {0}m" -f ($range))
            Write-Output ("rotation : {0}" -f ($ScriptOutput))

            if ( $ScriptOutput -gt 0.0 )
            {
                Write-Output "shear centre is further in"
                $UB = $trial
            }
            if ( $ScriptOutput -lt 0.0 )
            {
                Write-Output "shear centre is further out"
                $LB = $trial
            }
            Write-Output ("LB : {0}" -f ($LB))
            Write-Output ("UB : {0}" -f ($UB))
        }
        $entry  = [pscustomobject]@{
                "loading_z" = $loading_z
                'LB' = $LB
                'UB' = $UB
                'rotation=' = $ScriptOutput
            }
       
        $entry | Export-CSV  "E:\temp\NACA0025\outfile.csv" -Append

        $loading_z = $loading_z + 1
        $LB = -0.3
        $UB = -0.1
        $ScriptOutput = 0.1
    }
