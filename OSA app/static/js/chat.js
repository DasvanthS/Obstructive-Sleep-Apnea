

window.watsonAssistantChatOptions = {
    integrationID: "1df8b62f-ee5c-42bb-9a2f-6edcb89d85f7", // The ID of this integration.
    region: "jp-tok", // The region your integration is hosted in.
    serviceInstanceID: "ee519db2-aba8-4373-a6a2-e4e6fea336d7", // The ID of your service instance.
    onLoad: function(instance) { instance.render(); }
};
setTimeout(function(){
    const t=document.createElement('script');
    t.src="https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion ||
    'latest') + "/WatsonAssistantChatEntry.js";
    document.head.appendChild(t);
});

















