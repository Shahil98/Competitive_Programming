class Solution {
public:
    int lengthOfLastWord(string s)
    {
        int count = 0;

        int start = s.length()-1;

        for(int i=start; i>=0; i--)
        {
            if(s[i]==' ')
            {
                start--;
            }
            else
            {
                break;
            }
        }

        for(int i = start; i>=0; i--)
        {
            if(s[i]==' ')
            {
                break;
            }
            else
            {
                count++;
            }
        }
        return(count);
    }
};
