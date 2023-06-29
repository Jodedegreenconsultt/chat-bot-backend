from flask import Blueprint, request, jsonify
from services.pinecone import ChatbotService

pineconeRouter = Blueprint('pinecone', __name__)

chatbot_service = ChatbotService()


@pineconeRouter.route('query/modification/index/namespace',  methods=['POST'])
def QueryOnSpecificIndexWithNamespaceWithQueryModification():

    index = request.json.get('index')
    query = request.json.get('query')
    namespace = request.json.get('namespace')

    return chatbot_service.chatbot_query_using_openai_in_stream(index, namespace, query)
