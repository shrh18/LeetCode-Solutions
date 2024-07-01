// Solution for snowflake coding round

public class WordGenerator {
    public static void main(String[] args) {
        int wordLen = 37; // length of the word
        int maxVowels = 20; // maximum number of consecutive vowels
        
        int totalWords = generateWords(wordLen, maxVowels);
        System.out.println("Total unique words: " + totalWords);
    }
    
    public static int generateWords(int wordLen, int maxVowels) {
        // Base case: if word length is 0, return 1
        if (wordLen == 0) {
            return 1;
        }
        
        int totalWords = 0;
        
        // Generate words starting with a vowel
        if (maxVowels > 0) {
            totalWords += generateWords(wordLen - 1, maxVowels - 1) * 5; // 5 vowels: a, e, i, o, u
        }
        
        // Generate words starting with a consonant
        totalWords += generateWords(wordLen - 1, maxVowels) * 21; // 21 consonants
        
        return totalWords;
    }
}