#include<bits/stdc++.h>
using namespace std;

int partition(vector<int>& nums, int low, int high) 
{
    int pivot = nums[high];
    int i = low - 1;

    for (int j = low; j < high; ++j) 
    {
        if (nums[j] <= pivot) 
        {
            i++;
            swap(nums[i], nums[j]);
        }
    }

    swap(nums[i + 1], nums[high]);
    return i + 1;
}
int findKthLargest(vector<int>& nums, int k)
{
   int low = 0;
    int high = nums.size() - 1;

    while (low <= high) 
    {
        int pivotPos = partition(nums, low, high);
        
        if (pivotPos == nums.size() - k) {
            return nums[pivotPos];
        } else if (pivotPos > nums.size() - k) {
            high = pivotPos - 1;
        } else {
            low = pivotPos + 1;
        }
    }

    return -1; 
}
int main()
{
    
    int elements;
    cin>>elements;
    vector<int> nums(elements);
    for(int i=0;i<elements;i++)
    {
        cin>>nums[i];
    }
    int k;
    cin>>k;
    cout<<findKthLargest(nums, k)<<endl;
}