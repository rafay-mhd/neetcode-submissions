class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        List<Character> list1 = new ArrayList<>();
        List<Character> list2 = new ArrayList<>();
        for(char c : s.toCharArray()){
            list1.add(c);
        }
        for(char c : t.toCharArray()){
           list2.add(c);
        }
        Collections.sort(list1);
        Collections.sort(list2);

        //for(int i = 0; i < list1.size(); i++){
        //    if(list1.get(i) != list2.get(i)){
        //        return false;
        //    }
        //}
        //return true;
        return list1.equals(list2);
    }
}
