urls_file="check.txt"
dorks_file="$HOME/lists/dork.txt"

start_date=$(date -d "30 days ago" +"%Y-%m-%d")
end_date=$(date +"%Y-%m-%d")

while IFS= read -r url; do
  while IFS= read -r dork; do
    dork_with_dates="${dork//<dates>/after:$start_date before:$end_date}"
    banshee -u "$url" -q "$dork_with_dates" -p 3 -d 4 | anew pdfs.txt | notify -silent -id pdfs -d 2 -bulk
    sleep 1
  done < "$dorks_file"
done < "$urls_file"
