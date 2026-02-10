#!/usr/bin/env bash
# Bash String Manipulation - Hands-on Practice with Comments
# All examples are from the lesson + verified outputs (as of Bash 5.x)
# Correction: filename length is 23, not 24 (miscount fixed)

echo "=== 1. String Length =========================================="
greeting="Hi there"
filename="photo_2025_vacation.jpg"

echo '${#greeting}  → ' "${#greeting}"     # 8   (Hi<space>there)
echo '${#filename} → ' "${#filename}"      # 23  (photo_2025_vacation.jpg - corrected count)
echo

echo "=== 2. Substring Extraction =================================="
text="Hello World"

echo '${text:1:3}         → ' "${text:1:3}"            # ell
echo '${text:3:6}         → ' "${text:3:6}"            # lo Wor
echo '${text: -3}         → ' "${text: -3}"            # rld    (note: space before -3 is required in some shells)
echo '${text:${#text}-3}  → ' "${text:${#text}-3}"     # rld    (portable way without negative index)
echo '${text:100}         → ' "${text:100}"            # (empty string - start beyond end)
echo

echo "=== 3. Remove Prefix (from beginning) ========================"
path="projects/2025/january/report-v1-final.pdf"

echo '${path##*/}          → ' "${path##*/}"                 # report-v1-final.pdf          (longest prefix up to last /)
echo '${path#*2025/}       → ' "${path#*2025/}"              # january/report-v1-final.pdf  (shortest match after 2025/)
echo '${path#*/}           → ' "${path#*/}"                  # 2025/january/report-v1-final.pdf
echo '${path##projects/}   → ' "${path##projects/}"          # 2025/january/report-v1-final.pdf
echo

echo "=== 4. Remove Suffix (from end) + Date extraction ============="
archive="backup_2025-01-31_full_system.tar.gz.bak"

echo '${archive%.bak}              → ' "${archive%.bak}"                   # ...tar.gz
echo '${archive%%.*}               → ' "${archive%%.*}"                    # backup_2025-01-31_full_system   (greediest)
echo '${archive%.tar.gz.bak}       → ' "${archive%.tar.gz.bak}"            # ...full_system
echo '${archive%.gz.bak}           → ' "${archive%.gz.bak}"                # ...tar

# Clean way to extract just the date part (2025-01-31)
date_part="${archive#backup_}"     # remove prefix "backup_"
date_part="${date_part%%_*}"       # remove everything from first _ onward
echo 'Date extracted           → ' "$date_part"                            # 2025-01-31
echo

echo "=== 5. Pattern Replacement ===================================="
sentence="I like cats and cats and dogs and cats"

echo '${sentence/cats/birds}       → ' "${sentence/cats/birds}"
# → I like birds and cats and dogs and cats     (only first match)

echo '${sentence//cats/birds}      → ' "${sentence//cats/birds}"
# → I like birds and birds and dogs and birds   (all matches)

echo '${sentence// /-}             → ' "${sentence// /-}"
# → I-like-cats-and-cats-and-dogs-and-cats      (spaces → hyphen)

# Full upper + replace beginning (using pipe - common real-world pattern)
echo "${sentence//cats/BIRDS}" | tr '[:lower:]' '[:upper:]' | sed 's/I LIKE/I LOVE/'
# → I LOVE BIRDS AND BIRDS AND DOGS AND BIRDS

# Pure parameter expansion version (no external commands)
upper="${sentence//cats/BIRDS}"
echo '${upper/I like/I LOVE}       → ' "${upper/I like/I LOVE}"
# → I LOVE BIRDS and BIRDS and dogs and BIRDS   (note: only first "I like" changed)
echo

echo "=== Done! ====================================================="
# echo "You have now seen and run all core Bash string parameter expansions."
# echo "Tip: Combine them in real scripts (e.g. clean filenames, parse logs, build slugs)."