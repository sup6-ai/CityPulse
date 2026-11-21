#echo "enter input"
#read num

#echo $sum

#read -p "enter number" sum

#echo $sum



read -p "Enter your name: " name
read -p "Enter your roll number: " roll_no
read -p "Enter your comment: " comment

echo "Name: $name"
echo "Roll Number: $roll_no"
echo "Comment: $comment"

mkdir priya
touch priya/hello.txt
echo "Name: $name" > priya/hello.txt
echo "Roll Number: $roll_no" >> priya/hello.txt
echo "Comment: $comment" >> priya/hello.txt
cat priya/hello.txt

