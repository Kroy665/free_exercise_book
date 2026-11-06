// Strings that appear *inside study content* (question parts, note callouts).
// They follow the content language, not the UI language. The UI itself is English (i18n/en.json).
export const contentStrings: Record<string, Record<string, string>> = {
  en: {
    "callout.keyfacts": "Key facts",
    "callout.exam-tip": "Exam tip",
    "callout.mnemonic": "Memory aid",
    "callout.caution": "Common confusion",
    "callout.timeline": "Timeline",
    "callout.asof": "As of",
    "q.list1": "List I",
    "q.list2": "List II",
    "q.assertion": "Assertion (A)",
    "q.reason": "Reason (R)",
    "ar.0": "Both A and R are true, and R is the correct explanation of A",
    "ar.1": "Both A and R are true, but R is not the correct explanation of A",
    "ar.2": "A is true, but R is false",
    "ar.3": "A is false, but R is true",
  },
  bn: {
    "callout.keyfacts": "মূল তথ্য",
    "callout.exam-tip": "পরীক্ষার টিপস",
    "callout.mnemonic": "মনে রাখার কৌশল",
    "callout.caution": "সাধারণ বিভ্রান্তি",
    "callout.timeline": "সময়রেখা",
    "callout.asof": "তারিখ অনুযায়ী",
    "q.list1": "তালিকা I",
    "q.list2": "তালিকা II",
    "q.assertion": "বিবৃতি (A)",
    "q.reason": "কারণ (R)",
    "ar.0": "A ও R উভয়ই সত্য এবং R হলো A-এর সঠিক ব্যাখ্যা",
    "ar.1": "A ও R উভয়ই সত্য, কিন্তু R, A-এর সঠিক ব্যাখ্যা নয়",
    "ar.2": "A সত্য, কিন্তু R মিথ্যা",
    "ar.3": "A মিথ্যা, কিন্তু R সত্য",
  },
};

/** Content languages the user can pick (UI stays English). */
export const CONTENT_LANGS = [
  { code: "en", label: "English", native: "English" },
  { code: "bn", label: "Bengali", native: "বাংলা" },
] as const;
