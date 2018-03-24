while read -r -u 2 f1
do
        perl ~/Downloads/topd_v4.6.pl -f $f1 -m nodal -c multiple > $f1.result
done 2<filelist