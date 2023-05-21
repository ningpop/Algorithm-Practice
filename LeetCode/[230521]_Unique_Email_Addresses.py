class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        for email in emails:
            splited_email = email.split('@')
            host_name = splited_email[0]
            domain_name = splited_email[1]

            new_host_name = ''
            for c in host_name:
                if c == '.':
                    continue
                if c == '+':
                    break
                new_host_name += c
            
            result.add(new_host_name + '@' + domain_name)
        
        return len(result)