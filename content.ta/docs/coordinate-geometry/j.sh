#!/usr/bin/env bash

declare -a sections=(
"1|அறிமுகம்|introduction"
"2|ஆயத்தொலை வடிவியல்|coordinate-geometry"
"3|இரு புள்ளிகளுக்கு இடைப்பட்ட தொலைவு|distance-between-two-points"
"4|பிரிவு விகிதம்|section-formula"
"5|முக்கோணத்தின் பரப்பளவு|area-of-a-triangle"
"6|நேர்க்கோட்டின் சாய்வு|slope-of-a-straight-line"
"7|நேர்க்கோட்டின் சமன்பாடு|equation-of-a-straight-line"
"8|இணை மற்றும் செங்குத்து நேர்க்கோடுகள்|parallel-and-perpendicular-lines"
)

for item in "${sections[@]}"; do
    IFS="|" read -r weight title slug <<< "$item"

    cat > "${slug}.md" <<EOF
---
title: '$title'
weight: $weight
---
EOF

    echo "Created ${slug}.md"
done