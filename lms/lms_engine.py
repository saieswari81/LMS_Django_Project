def lms_engine(p_cust_cs, p_cust_req_loan_amt, p_loan_rules):
    l_is_success = 0
    p_loan_id = 0
    result = {'loan_type': p_loan_id, 'interest': 0, 'duration': 0, 'success': l_is_success}
    for c in p_loan_rules:
        if p_cust_cs >= c["cs_start"] and p_cust_cs <= c["cs_end"] and \
                p_cust_req_loan_amt >= c["loan_amt_start"] and p_cust_req_loan_amt <= c["loan_amt_end"]:
            # print(p_cust_name)
            # print(c["interest"])
            # print(c["duration_in_months"])
            l_is_success = 1
            result['interest'] = c["interest"]
            result['duration'] = c["duration_in_months"]
            result['success'] = l_is_success
            break

    return result
