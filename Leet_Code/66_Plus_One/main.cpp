class Solution {
public:
    vector<int> plusOne(vector<int>& digits)
    {
        int n = digits.size()-1;

        if(n < 0)
        {
            return(digits);
        }

        while(true and n>=0)
        {
            if(digits[n] == 9)
            {
                digits[n] = 0;
                n--;
            }

            else
            {
                break;
            }

        }

        if(n<0)
        {
            digits[0] = 1;
            digits.push_back(0);
        }

        else
        {
            digits[n]++;
        }

        return(digits);
    }
};
