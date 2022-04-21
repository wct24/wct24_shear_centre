
#initial
$LB = 0.5
$UB = 0.52
$ScriptOutput = 0.1

$increment =  0.000001

$lambda = 0
$sim_number = 0
while($lambda -lt 10)
    {

        while(($UB-$LB -gt $increment) )
        {

            $a = ($UB-$LB)/2
            $trial = $LB+$a

            python intermediate.py $trial $lambda

            $sim_number =  $sim_number + 1
            Write-Output ("Simulation Number : {0}" -f ($sim_number))
            Write-Output ("Lambda: {0}/9" -f ($lambda) )

            abaqus cae noGUI=semi-circle_script.py

            $find_shear_center="C:\Users\touze\project\Shear_centre\semi_circle\effect_of_lambda\find_shear_centre.py"
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
                "lambda" = $loading_z
                'LB' = $LB
                'UB' = $UB
                'rotation=' = $ScriptOutput
            }
        $entry | Export-CSV  "E:\temp\SC\outfile.csv" -Append
        python plot_rotation.py
        $lambda = $lambda+ 1
        $LB = 0.5
        $UB = 0.52
        $ScriptOutput = 0.1
    }
