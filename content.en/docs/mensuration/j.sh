#!/usr/bin/env bash

declare -a sections=(
"1|Introduction"
"2|Surface Area"
"3|Volume"
"4|Volume and Surface Area of Combined Solids"
"5|Conversion of Solids from one Shape to another with no change in Volume"
)

slugify() {
    echo "$1" \
        | tr '[:upper:]' '[:lower:]' \
        | sed "s/[’']//g" \
        | sed 's/[^a-z0-9]/-/g' \
        | sed 's/-\+/-/g' \
        | sed 's/^-//' \
        | sed 's/-$//'
}

for item in "${sections[@]}"; do
    weight="${item%%|*}"
    title="${item#*|}"
    file="$(slugify "$title").md"

    cat > "$file" <<EOF
---
title: '$title'
weight: $weight
---
EOF

    echo "Created $file"
done