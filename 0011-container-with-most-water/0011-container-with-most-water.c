int maxArea(int* height, int heightSize) 
{
    int left = 0, right = heightSize - 1;
    int maxArea = 0;

    while (left < right) {
        int h = fmin(height[left], height[right]);
        int w = right - left;
        int currentArea = h * w;

        maxArea = fmax(maxArea, currentArea);

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxArea;
}





