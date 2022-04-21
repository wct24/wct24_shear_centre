
#initial
$lambda = 0.1
$UB = 3.0
$ScriptOutput = 0.1


while($lambda -lt $UB )
{
    Write-Output $lambda
    python intermediate.py $lambda

    abaqus cae noGUI=strip_script.py
    $script="C:\Users\touze\project\Shear_centre\strip\postprocessing.py"
    $ScriptOutput=[double]$( python $script)
    Write-Output $ScriptOutput
    $lamb = $lambda
    $entry  = [pscustomobject]@{
        'lambda' = $lambda
        'length' = $ScriptOutput

    }
    $entry | Export-CSV  "E:\temp\strip\outfile.csv" -Append

    $lambda = $lambda + 0.01
}
