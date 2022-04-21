
#initial

$ScriptOutput = 0.1

$beam_number = 68
while($beam_number -lt 107)
    {
    python intermediate.py $beam_number

    Write-Output ("Section: {0}/106" -f ($beam_number))

    abaqus cae noGUI=I-beam_script.py
    abaqus cae noGUI=Get_area_script.py


    $warping_analysis="C:\Users\touze\project\Shear_centre\I-beam\warping_analysis.py"
    $ScriptOutput=[double]$( python $warping_analysis)

    $entry  = [pscustomobject]@{
            "beam_number" = $beam_number
            'gamma=' = $ScriptOutput
        }
    $entry | Export-CSV  "E:\temp\I\outfile.csv" -Append

    $beam_number = $beam_number + 1
    }
