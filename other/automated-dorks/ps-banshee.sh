urls_file="check.txt"
dorks_file="~/lists/dork.txt"
output_file="banshee_results.txt"

start_date=$(date -d "7 days ago" +"%Y-%m-%d")
end_date=$(date +"%Y-%m-%d")

cat /dev/null > "$output_file"

while IFS= read -r url; do
  while IFS= read -r dork; do
    dork_with_dates="${dork//<dates>/after:$start_date before:$end_date}"
    
    temp_file="temp_results.txt"
    banshee -u "$url" -q "$dork_with_dates" -p 2 -d 4 > "$temp_file" # -a
    
    if [ -s "$temp_file" ]; then
      echo "URL: $url | Dork used: $dork_with_dates" | anew "$output_file"
      cat "$temp_file" | anew "$output_file"
      echo "----" | anew "$output_file"
    fi
    
    rm -f "$temp_file"
    
    sleep 1
  done < "$dorks_file"
done < "$urls_file"

cat "$output_file" | notify -id pdfs -d 3
mv "$output_file" tmp/banshee.$(date +%s).txt