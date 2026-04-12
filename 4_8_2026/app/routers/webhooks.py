from fastapi import APIRouter,Request
import logging

router = APIRouter(prefix='/api/webhook',tags=['Webhooks'])

@router.post('/n8n/transaction')
async def recieve_from_n8n(request:Request):
    """
    n8n send classified/processed data back here
    
    """

    payload = await request.json()
    logging.info(f'Recieved from n8n:{payload}')

    return { 'status':'recieved','data':payload }



@router.post('/n8n/alert')
async def recieve_alrt(request:Request):
    payload = await request.json()
    logging.info(f"Recieve fron n8n:{payload}")
    return {'status':'alert_processed'}