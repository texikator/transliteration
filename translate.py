import iuliia
import sys
from flask import Flask, abort, request, jsonify, make_response

app = Flask(__name__)

args = sys.argv
# print(args)
# if len(args) == 2:
#     schema = "MOSMETRO"
# else:
#     schema = args[2]


#source_text = args[1]
def translate_text(source, encoding):
    
    schema = iuliia.Schemas.get(encoding)

    return iuliia.translate(source, schema)

def get_account_data(account_data, location="fields", enc='mosmetro'):
    if location == "fields":
        domain_name = "@jadran.ru"
    elif location == "office":
        domain_name ="@jgl.ru"
    
    else:
        domain_name = '@jgl.ru'

    account_transliterated = translate_text(account_data, enc).split()
    a_family = account_transliterated[0]
    a_name = account_transliterated[1]
    logon_name = f'{a_name[:1]}{a_family}'
    full_name = f'{a_family}, {a_name}'
    a_email = f'{logon_name}{domain_name}'

    return {'logon_name': logon_name, 'full_name': full_name, 'email':a_email }


@app.route('/transliterate/api/v1.0/simple', methods=['POST'])
def simple_translit():
    print(request.json)
    print(request.args)
    if not request.json or not 'text' in request.json:
        abort(400)
    encoding = request.json.get('enc','mosmetro')
    text = request.json['text']
    transliterated_text = translate_text(text, encoding)
    return jsonify({'data':{'text': transliterated_text}}), 201



@app.route('/transliterate/api/v1.0/detailed', methods=['POST'])
def get_detailed_info():

    print(request.json)

    if not request.json or not 'account_data' in request.json:
        abort(400)
    print(request.json['account_data'])
    print(request.json['location'])
    #print(request.json['enc'])
    print(request.json.get('enc','mosmetro'))


    account_data = request.json['account_data']
    location = request.json['location']
    enc = request.json.get('enc', 'mosmetro')
    result = get_account_data(account_data, location, enc)

    return jsonify({'data': result}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    #source = "миру мымр Артыбаева Агайлым"
    #print(translate_text(source))
    #print(translate_text(source, 'wikipedia'))
    if sys.argv[1] == 'simple':
        print(get_account_data(input('ФИ'),"office")) 
    else:#print(get_account_data('Бахитов Тимур',"office"))
        app.run(debug=True, host="0.0.0.0")
