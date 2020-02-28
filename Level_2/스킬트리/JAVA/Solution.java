class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = skill_trees.length;
        int prevIndex = 0, currentIndex = 0;
        
        for (int i = 0; i < skill_trees.length; i++) {
            prevIndex = skill_trees[i].indexOf(skill.charAt(0));
            
            for (int j = 0; j < skill.length(); j++) {
                currentIndex = skill_trees[i].indexOf(skill.charAt(j));
                if ((prevIndex > currentIndex && currentIndex != -1) || (prevIndex == -1 && currentIndex != -1)) {
                 answer--;
                    break;
                }
                prevIndex = currentIndex;
            }
        }
        return answer;
    }
}