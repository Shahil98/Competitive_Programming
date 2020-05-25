class Solution {
public:

    //Heapify function
    void heapify(vector<vector<int>>& arr, int index, int n)
    {
        int new_index = index;
        int left = (index+1)*2 - 1;
        int right = (index+1)*2;

        if(left <= (n-1))
        {
            if(arr[new_index][0] > arr[left][0])
            {
                new_index = left;
            }

        }

        if(right <= (n-1))
        {
            if(arr[new_index][0] > arr[right][0])
            {
                new_index = right;
            }
        }

        if(new_index != index)
        {
            int temp = arr[index][0];
            arr[index][0] = arr[new_index][0];
            arr[new_index][0] = temp;

            temp = arr[index][1];
            arr[index][1] = arr[new_index][1];
            arr[new_index][1] = temp;

            heapify(arr, new_index, n);
        }

        /*
        if((index+1)*2 <= n)
        {
            if(arr[(index+1)*2 - 1][0] < arr[index][0])
            {
                int temp = arr[(index+1)*2 - 1][0];
                arr[(index+1)*2 - 1][0] = arr[index][0];
                arr[index][0] = temp;

                temp = arr[(index+1)*2 - 1][1];
                arr[(index+1)*2 - 1][1] = arr[index][1];
                arr[index][1] = temp;

                new_index = (index+1)*2 - 1;
            }
        }

        if(((index+1)*2 + 1) <= n)
        {
            if(arr[(index+1)*2][0] < arr[index][0])
            {
                int temp = arr[(index+1)*2][0];
                arr[(index+1)*2][0] = arr[index][0];
                arr[index][0] = temp;

                temp = arr[(index+1)*2][1];
                arr[(index+1)*2][1] = arr[index][1];
                arr[index][1] = temp;

                new_index = (index+1)*2;
            }
        }



        if(new_index != index)
        {
            heapify(arr, new_index, n);
        }

        */
    }

    vector<vector<int>> merge(vector<vector<int>>& intervals)
    {
        int n = intervals.size();

        if(n == 0)
        {
            return(intervals);
        }

        int heap_n = int(n/2) - 1;

        /*
        if(n%2 == 0)
        {
            heap_n = n/2-1;
        }
        else
        {
            heap_n = n/2;
        }
        */


        //Building heap
        for(int i=heap_n; i>=0; i--)
        {
            heapify(intervals,i,n);
        }

        //Sorting
        vector<vector<int>> new_intervals;

        while(n != 0)
        {

            int temp = intervals[0][0];
            intervals[0][0] = intervals[n-1][0];
            intervals[n-1][0] = temp;

            temp = intervals[0][1];
            intervals[0][1] = intervals[n-1][1];
            intervals[n-1][1] = temp;

            new_intervals.push_back(intervals[n-1]);

            heapify(intervals,0,n-1);

            n = n-1;
        }

        n = intervals.size();

        vector<vector<int>> output_intervals;

        int cur_index = 0;

        //generating intervals
        if(n > 0)
        {
            output_intervals.push_back(new_intervals[0]);

            for(int i=1; i<n; i++)
            {
                if((output_intervals[cur_index][0] <= new_intervals[i][0]) && ((output_intervals[cur_index][1] >= new_intervals[i][0])) )
                {
                    if(new_intervals[i][1] > output_intervals[cur_index][1])
                    {
                        output_intervals[cur_index][1] = new_intervals[i][1];
                    }
                }
                else
                {
                    cur_index++;
                    output_intervals.push_back(new_intervals[i]);
                }
            }
        }

        return(output_intervals);

    }
};
