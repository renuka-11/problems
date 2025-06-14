class Solution {
    public int minMaxDifference(int num) {
        String str = String.valueOf(num);
        int max=Integer.MIN_VALUE;
        int min=Integer.MAX_VALUE;
        if(str.length()>0){
            for(int i=0;i<str.length();i++){
                char target = str.charAt(i);
                String maxStr=str.replace(target,'9');
                int maxVal = Integer.parseInt(maxStr);
                max=Math.max(max,maxVal);
                String minStr=str.replace(target,'0');
                int minVal = Integer.parseInt(minStr);
                min=Math.min(min,minVal);

            }
            return max-min;

        }
        return 0;
        
    }
}
