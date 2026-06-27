git pull origin main

echo "Syncing Study System..."

python system/build_mistakes.py
python system/build_review.py

git add .
git commit -m "auto sync update"
git push origin main
