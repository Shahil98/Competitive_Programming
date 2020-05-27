class Solution {
public:

    map<int,int> factorial_cache;

    void factorial(int n)
    {
        int f = 1;

        for(int i=1; i<=n; i++)
        {
            f = f*i;
            factorial_cache[i] = f;
        }

    }

    int selectNumber(int fac, int k, vector<int>& arr, vector<int>& permutationArray)
    {
        int index = 0;

        int num = fac/arr.size();

        while(true)
        {
            if((num*(index+1)) < k)
            {
                index++;
            }

            else
            {
                break;
            }
        }

        permutationArray.push_back(arr[index]);
        arr.erase(arr.begin()+index);

        return((num*(index)));
    }

    string getPermutation(int n, int k)
    {

        vector<int> permutationArray;
        vector<int> arr;

        for(int i=1; i<=n; i++)
        {
            arr.push_back(i);
        }

        factorial(n);

        for(int i=n; i>=1; i--)
        {
            k = k - selectNumber(factorial_cache[i], k, arr, permutationArray);
        }

        string permutation;

        for(int i=0; i<n; i++)
        {
            permutation = permutation + to_string(permutationArray[i]);
        }

        return(permutation);
    }
};
